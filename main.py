# -*- coding: utf-8 -*-
"""NLA_Project_submit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HWshTVjkuduoEVu1IYV30B1xMRsD95Lv
"""

#Import libraries
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
import pandas as pd
from sklearn.decomposition import PCA

def create_portfolio(n):
  '''
  Function creates a portfolio of size n.
  '''
  S0 = 100.0             # asset price
  T = 1.0                # time in years
  r = 0.02               # risk-free rate
  N = 10000              # number of time steps in simulation
  M = 1                  # number of simulations
  kappa = 3              # rate of mean reversion of variance under risk-neutral dynamics
  theta = 0.21**2        # long-term mean of variance under risk-neutral dynamics
  v0 = 0.26**2           # initial variance under risk-neutral dynamics
  sigma = 0.55
  delta = 0.0001
  Portfolio = []
  for i in range(n):
    S = S0
    kappa = kappa+i*delta
    theta = theta+i*delta
    v0 = v0+i*delta
    sigma = sigma+i*delta
    instrument = [S, kappa, theta, v0, sigma]
    Portfolio.append(instrument)
  return Portfolio

def create_portfolio_mean(Portfolio):
  '''
  Function creates a mean portfolio witch is used for Monte Carlo simulations after PCA
  '''
  S_m = 0
  kappa_m = 0
  theta_m = 0
  v0_m = 0
  sigma_m = 0
  for i in range(len(Portfolio)):
    S_m+=Portfolio[i][0]
    kappa_m+=Portfolio[i][1]
    theta_m+=Portfolio[i][2]
    v0_m+=Portfolio[i][3]
    sigma_m+=Portfolio[i][4]
  S_m = S_m/n
  kappa_m = kappa_m / n
  theta_m = theta_m / n
  v0_m = v0_m / n
  sigma_m = sigma_m/n
  Mean_portfolio = [S_m,kappa_m,theta_m,v0_m,sigma_m]
  return Mean_portfolio

def create_cov(n):
  '''
  Function creates a random covariance matrix of size n
  '''
  A = np.zeros((n,n))
  for i in range(n):
    for j in range(n):
      cov_rand = float(np.random.rand(1,1))
      A[i][j] = cov_rand
      A[j][i] = cov_rand
      A[i][i] = 1
  return A

def validate_cov_matrix(A):
     """
     Function validates covariance matrix for positive semidefinite property and update matrix
     """
     A = (A + A.T) * 0.5
     k = 0
     I = np.eye(A.shape[0])
     while True:
         try:
             _ = np.linalg.cholesky(A)
             break
         except np.linalg.LinAlgError:
             k += 1
             w, v = np.linalg.eig(A)
             min_eig = v.min()
             A += (-min_eig * k * k + np.spacing(min_eig)) * I
     return A

def create_correlated_GBMs(n):
  """
  Function creates n correlated Geometric Brownian motions of size N using Cholesky decomposition
  """
  N = 10000
  M = 1
  A = create_cov(n)
  B = validate_cov_matrix(A)

  rng = np.random.default_rng()
  mu = np.zeros(n)
  Z = rng.multivariate_normal(mu, B, (N,M), check_valid='ignore', method='cholesky')
  return Z

def create_dataset(Z):
  """
  Function creates dataset from correlated GBMs
  """
  new_img = Z.reshape((Z.shape[0]*Z.shape[1]), Z.shape[2])
  labels = []
  for i in range(n):
    labels.append(str(i))
  dataset = pd.DataFrame(new_img, columns = labels)
  return dataset

