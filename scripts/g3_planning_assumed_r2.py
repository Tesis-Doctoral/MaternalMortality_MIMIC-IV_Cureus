"""Gate G3, planning step: minimum sample size with an assumed Cox-Snell R2 (15% of its maximum, the conservative
default of Riley et al.), before any candidate model is fitted. Uses only aggregate counts (no database access).
The reassessment step, with the observed out-of-fold R2, is in notebooks 03, 07 and 10.
Writes data/outputs_g3_planning.txt. Run from the repository root: python scripts/g3_planning_assumed_r2.py
"""
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# (outcome, candidate parameters, admissions, events): counts of notebooks 03 and 07 (aggregates)
CASES = [("maternal death (M1)", 32, 19383, 3),
         ("SMM, main model (M2)", 32, 19383, 445),
         ("SMM, return R4 (extended laboratory set)", 54, 19383, 445),
         ("escalation of care (return R2)", 32, 19268, 101),
         ("escalation of care, sample-size reduction", 13, 19268, 101)]
SHARE_OF_MAX = 0.15

def riley(P, phi, r2, shrink=0.9):
    lnl0 = phi * math.log(phi) + (1 - phi) * math.log(1 - phi)
    max_r2 = 1 - math.exp(2 * lnl0)
    n1 = P / ((shrink - 1) * math.log(1 - r2 / shrink))
    s = r2 / (r2 + 0.05 * max_r2)
    n2 = P / ((s - 1) * math.log(1 - r2 / s))
    n3 = (1.96 / 0.05) ** 2 * phi * (1 - phi)
    n = max(n1, n2, n3)
    return max_r2, n1, n2, n3, n

lines = [f"GATE G3, PLANNING STEP: assumed Cox-Snell R2 = {SHARE_OF_MAX:.0%} of its maximum (Riley et al.)",
         "outcome | P | admissions | events | max R2 | assumed R2 | n shrinkage | n optimism | n risk | n required | events required | G3"]
for name, P, n, e in CASES:
    phi = e / n
    mx, n1, n2, n3, req = riley(P, phi, SHARE_OF_MAX * riley(P, phi, 0.01)[0])
    r2 = SHARE_OF_MAX * mx
    lines.append(f"{name} | {P} | {n} | {e} | {mx:.4f} | {r2:.4f} | {n1:.0f} | {n2:.0f} | {n3:.0f} | {req:.0f} | "
                 f"{req * phi:.0f} | {'passes' if req <= n and req * phi <= e else 'does NOT pass'}")
text = "\n".join(lines) + "\n"
print(text)
(ROOT / "data" / "outputs_g3_planning.txt").write_text(text, encoding="utf-8")
