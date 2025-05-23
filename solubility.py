import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from rdkit import Chem
from rdkit.Chem import Descriptors

def plot_pca(T, labels):
    plt.figure(figsize=(5, 4))
    for i, (label, color) in enumerate(zip(sorted(set(labels)), ('green', 'gray', 'red'))):
        plt.scatter(T[labels == label, 0], T[labels == label, 1], label=label,
                    marker=str(i+1), color=color, linewidth=1.0)
    plt.axline([0, 0], [1, 0], linestyle='--', linewidth=0.8, color='gray')
    plt.axline([0, 0], [0, 1], linestyle='--', linewidth=0.8, color='gray')
    plt.xlim(-10, 25)
    plt.ylim(-20, 15)
    plt.legend()
    plt.savefig('figure/solubility_PCA.png', dpi=100)

def pca(X, columns):
    N, n = X.shape

    # Mean centering.
    X = X - np.mean(X, axis=0)

    # Standardization.
    X = X / np.std(X, axis=0)

    U, S, Vt = np.linalg.svd(X)
    T = U[:, :n] * S

    importance = pd.DataFrame(zip(columns, Vt.T[:, 1]), columns=['feature', 'value'])

    return T, importance

def load_dataset():
    descriptors, y, labels = [], [], []
    for mol in Chem.SDMolSupplier('data/solubility.train.sdf'):
        descriptors.append(Descriptors.CalcMolDescriptors(mol))
        y.append(np.float32(mol.GetProp('SOL')))
        labels.append(mol.GetProp('SOL_classification'))

    data = []
    for descriptor in descriptors:
        data.append(descriptor.values())

    X = pd.DataFrame(data, columns=descriptor.keys())

    labels = np.asarray(labels)

    return X, y, labels

def main():
    X, y, labels = load_dataset()

    print(pd.DataFrame(labels, columns=['label']).groupby('label').size())

    print('Exclude {} features of the NaN values.'.format((X.isnull().sum(axis=0) > 0).sum()))
    X = X.loc[:, X.isnull().sum(axis=0) == 0]

    print('Exclude {} features of zero variance.'.format((X.var(axis=0) == 0).sum()))
    X = X.loc[:, X.var(axis=0) != 0]

    T, importance = pca(X.values, X.columns)

    print(importance.sort_values('value', ascending=False))

    plot_pca(T, labels)

if __name__ == '__main__':
    main()
