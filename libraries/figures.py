# -*- coding: utf-8 -*-
"""Figures of the notebooks: ROC curves (one subplot per algorithm or population) and, for the final model, the
classification report next to the confusion matrix. Confusion-matrix counts are weighted to the full population
(non-events carry weight 1/FRACTION in the case-control samples). Labels follow the language of the notebook."""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score, roc_curve


def _tr(s, lang):
    from libraries.i18n import translate
    return translate(s, lang)


def _save(fig, fig_dir, fname, lang):
    fig_dir.mkdir(exist_ok=True)
    fig.tight_layout()
    fig.savefig(fig_dir / (fname.replace(".png", "_es.png") if lang == "es" else fname), dpi=200)
    plt.show()


def plot_roc(curves, title, fname, lang, fig_dir):
    """curves: list of (label, y, p). One subplot per curve, so the curves do not overlap; AUROC in each title.
    AUROC does not depend on the case-control weights."""
    n = len(curves); ncol = min(3, n); nrow = int(np.ceil(n / ncol))
    fig, axes = plt.subplots(nrow, ncol, figsize=(4.4 * ncol, 4.4 * nrow), squeeze=False)
    for k, (label, yy, pp) in enumerate(curves):
        ax = axes[k // ncol][k % ncol]
        fpr, tpr, _ = roc_curve(yy, pp)
        ax.plot(fpr, tpr, lw=1.8, color="#2F6DB5")
        ax.fill_between(fpr, tpr, alpha=0.08, color="#2F6DB5")
        ax.plot([0, 1], [0, 1], ls="--", color="grey", lw=1)
        ax.set_title(f"{_tr(label, lang)}\nAUROC {roc_auc_score(yy, pp):.3f}", fontsize=10)
        ax.set_xlim(0, 1); ax.set_ylim(0, 1.01); ax.set_aspect("equal")
        ax.set_xlabel(_tr("1 - specificity (false positive rate)", lang), fontsize=9)
        ax.set_ylabel(_tr("Sensitivity (true positive rate)", lang), fontsize=9)
    for k in range(n, nrow * ncol):
        axes[k // ncol][k % ncol].axis("off")
    fig.suptitle(_tr(title, lang), fontsize=12)
    _save(fig, fig_dir, fname, lang)


def cut_top(p, w, share):
    """Risk cut that flags the given share of the weighted population."""
    o = np.argsort(-p); cw = np.cumsum(w[o])
    return float(p[o][np.searchsorted(cw, share * cw[-1])])


def threshold_metrics(y, p, w, cut):
    """Accuracy, F1 and the confusion-matrix rates at a declared risk cut (weighted to the population)."""
    flag = p >= cut
    tp, fp = w[flag & y].sum(), w[flag & ~y].sum(); fn, tn = w[~flag & y].sum(), w[~flag & ~y].sum()
    sens, ppv = tp / (tp + fn), tp / (tp + fp)
    return {"risk cut": round(cut, 4), "TP": int(round(tp)), "FP": int(round(fp)), "FN": int(round(fn)), "TN": int(round(tn)),
            "accuracy": round(float((tp + tn) / (tp + fp + fn + tn)), 4), "F1": round(float(2 * sens * ppv / (sens + ppv)), 4),
            "sensitivity": round(float(sens), 4), "specificity": round(float(tn / (tn + fp)), 4),
            "PPV": round(float(ppv), 4), "NPV": round(float(tn / (tn + fn)), 5)}


def plot_report_cm(panels, fname, lang, fig_dir):
    """panels: list of (title, y, p, w, cut). Left: classification report of the two classes (precision, recall, F1,
    accuracy and macro average) as a heatmap; right: confusion matrix. Class 1 = the event of the model."""
    from sklearn.metrics import ConfusionMatrixDisplay
    fig, axes = plt.subplots(len(panels), 2, figsize=(12.5, 4.6 * len(panels)), squeeze=False,
                             gridspec_kw={"width_ratios": [1.35, 1]})
    for row, (title, yy, pp, ww, cut) in enumerate(panels):
        m = threshold_metrics(yy, pp, ww, cut)
        tp, fp, fn, tn = m["TP"], m["FP"], m["FN"], m["TN"]
        f1 = lambda a, b: 2 * a * b / (a + b) if (a + b) else 0.0
        p0, r0 = tn / (tn + fn), tn / (tn + fp)
        p1, r1 = tp / (tp + fp), tp / (tp + fn)
        acc = (tp + tn) / (tp + fp + fn + tn)
        rep = np.array([[p0, r0, f1(p0, r0)], [p1, r1, f1(p1, r1)], [acc, acc, acc],
                        [(p0 + p1) / 2, (r0 + r1) / 2, (f1(p0, r0) + f1(p1, r1)) / 2]])
        ax = axes[row][0]
        ax.imshow(rep, cmap="YlGnBu", vmin=0, vmax=1, aspect="auto")
        for i in range(rep.shape[0]):
            for j in range(rep.shape[1]):
                ax.text(j, i, f"{rep[i, j]:.2f}", ha="center", va="center", fontsize=10,
                        color="white" if rep[i, j] > 0.6 else "black")
        ax.set_xticks(range(3), [_tr(c, lang) for c in ("precision", "recall", "f1-score")])
        ax.set_yticks(range(4), ["0", "1", _tr("accuracy", lang), _tr("macro avg", lang)])
        ax.set_xlabel(_tr("Metrics", lang)); ax.set_ylabel(_tr("Classes", lang))
        ax.set_title(_tr(title, lang) + f" ({_tr('risk cut', lang)} {cut:.4f})", fontsize=9)
        ax2 = axes[row][1]
        ConfusionMatrixDisplay(confusion_matrix=np.array([[tn, fp], [fn, tp]]), display_labels=[0, 1]).plot(
            ax=ax2, cmap="Blues", colorbar=False, values_format=",d")
        ax2.set_xlabel(_tr("Predicted label", lang)); ax2.set_ylabel(_tr("True label", lang))
        ax2.set_title(_tr("Confusion matrix", lang), fontsize=9)
    _save(fig, fig_dir, fname, lang)
