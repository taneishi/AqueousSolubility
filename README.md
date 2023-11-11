# Representation of aqueous solubility of small molecules using PCA

## Introduction

*Small molecules* are still a large percentage of *drug discovery* candidates due to their ease of handling and use.
Screening is one of the initial steps in drug discovery for small molecules, and *virtual screening* is a computational approach to this process.

Virtual screening used *molecular descriptors* calculated from the structure of a compound as features, prior to the introduction of *deep learning*, DL.
Molecular descriptors are mainly composed of two components: experimental measurements such as physicochemical properties, and theoretically defined quantities such as geometric properties.
In particular, molecular descriptors that are determined from the existence and frequency of substructures, which is one of the geometrical properties, are called *chemical fingerprints*.

An early attempt to characterize *small molecule drugs* using molecular descriptors is known as the *rule of five* proposed by Lipinski et al. in 1997.
This is a proposal to represent the *absorption*, *distribution*, *metabolism*, and *excretion*, so-called ADME, of mainly oral drugs by using the *hydrogen bond donors*, *hydrogen bond acceptors*, *molecular weight*, and *partition coefficient* of small molecules as the features.
The concept that features represent in the virtual screening of small molecule drugs is called *druglikeness*, and ADME is considered to be a part of it.
As computing has progressed, a large number of compounds and features have been used for the representation of druglikeness by molecular descriptors.
There have been attempts to represent more complex properties of compounds by molecular descriptors, and *quantitative structure-activity relationship*, QSAR, which seeks correlation with biological acivities essential for small molecule drugs,is an early application of machine learning.

As an example here, we take the *aqueous solubility* of small molecules and project the molecular descriptors using PCA, to visually represent their properties.

## Dataset

We use the dataset from [Huuskonen], which was evaluated to predict the aqueous solubility of small molecules. 
This dataset contains 1,025 small molecules defined in MDL Molfile format and classified into 417, 402, and 206 categories according to low, medium, and high solubility, respectively.

The Python cheminformatics package `RDKit` was used to calculate molecular descriptors.
Of all molecular descriptors defined in `RDKit`, 183 molecular descriptors were used as features after excluding descriptors containing missing values.
Thus, each compound is represented by a real vector of 183 dimensions and the dataset is a $(1025 \times 183)$-matrix.

## Methods

PCA is the most fundamental *unsupervised* or *self-supervised learning*.
Mathematically, it is based on the eigendecomposition of the covariance matrix, and is a linear method that gives a projection from the original coordinates to the coordinates that maximize the variance in each dimension.
It is often used as the first choice in machine learning, especially in *visualization*, because it allows dimensionality reduction at a practical cost by extracting common features from a given dataset in high dimensions.

Here, we investigate the possibility of classifying solubility using a linear method by projecting the higher-dimensional molecular descriptor representation of the compounds onto the coordinate with the largest variance.

## Results

PCA is performed on the matrix of the given dataset using *singular value decomposition* and the results plotted by the two dimensions with the largest variance are shown in Figure 1.

![Relationship between the PCA projection of molecular descriptors and aqueous solubility of small molecules.](figure/solubility_PCA.png)

**Figure 1. Relationship between the PCA projection of molecular descriptors and aqueous solubility of small molecules.**

Compounds with high, medium, and low solubilities form clusters in the projected space, respectively.
Especially for compounds with high and low solubility, they are almost linearly separable.

## Furthermore

Molecular descriptors were often used as input in the early DL applications, but as the DL model evolved, the model required more features, and chemical fingerprints such as *Morgan fingerprints* or *extended-connectivity fingerprints*, ECFP, which are defined based on graphs of chemical structures, are used as high-dimensional features to represent compounds, and high accuracy has been achieved.

Because these chemical fingerprints based on graph structures have been effective, neural networks such as *graph convolutional networks*, GCN, which accept graph structures as input, were proposed as models for handling chemical compounds, without going through chemical fingerprints.

## Reference

- [Huuskonen] J. Huuskonen, *Estimation of Aqueous Solubility for a Diverse Set of Organic Compounds Based on Molecular Topology*, **J Chem Inf Comput Sci**, 40, 3, pp.773–777, 2000.
