# Monte-Carlo
In the realm of finance, our research addresses the challenge to speed up Monte Carlo simulations without significant loss in accuracy.   Experimental results aim to validate this hypothesis, offering insights to enhance investment strategies.
We prepared both py and ipynb versions. If someone wants to check results of experiments then open ipynb version with ready to watch plots, if someone want to start testing out solution you are free to use py version. 

Our solution proposes 4 steps:
1. Generate an n asset portfolio.
2. Generate GBM random correlated motions for each asset.
3. Use PCA to decrease the dimension of GBM's motions matrix
4. Use Monte Carlo to simulate processes.

Links to papers and guides that helped us:

1) https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4066115


2) https://sas.uwaterloo.ca/~dlmcleis/s906/chapt1-6.pdf


3) https://www.informs-sim.org/wsc07papers/107.pdf


4) https://arxiv.org/pdf/1903.10795v1.pdf


5) https://www.youtube.com/watch?v=o8C6DxZh8dw

All you need to start our project is just follow steps in ipynb file. But . . . Here an example: 
Define n as the number of assets. Then

For PCA Monte Carlo simulations:
n = 7
Portfolio = create_portfolio(n)
Mean_portfolio = create_portfolio_mean(Portfolio)
Z = create_correlated_GBMs(n)
dataset = create_dataset(Z)
principal_breast_Df = fast_PCA(dataset, n_components = 3)
T = 1.0                
N = 10000               
M = 1
fig, ax1  = plt.subplots(1, 1, figsize=(12,5))
time = np.linspace(0,T,N+1)
Means_pca = []
for j in range(principal_breast_Df.shape[1]):
  S = heston_model_sim2(Mean_portfolio[0], Mean_portfolio[3], Mean_portfolio[1], Mean_portfolio[2], Mean_portfolio[4],T, N, M, Z, ind = j, principal_breast_Df = principal_breast_Df[str(j)])
  Means_pca.append(S.mean())
  ax1.plot(time,S,label = '{}instrument'.format(j))

ax1.set_title('Heston Model Asset Prices')
ax1.set_xlabel('Time')
ax1.set_ylabel('Asset Prices')
plt.show()

For Basic Monte Carlo simulations:
fig, ax1  = plt.subplots(1, 1, figsize=(12,5))
time = np.linspace(0,T,N+1)
Means = []
for i in range(len(Portfolio)):
  S = heston_model_sim(S0 = Portfolio[i][0], v0 = Portfolio[i][3], kappa = Portfolio[i][1], theta = Portfolio[i][2], sigma = Portfolio[i][4],T=T, N=N, M=M, Z=Z, ind = i)
  Means.append(S.mean())
  ax1.plot(time,S,label = '{}instrument'.format(i))

ax1.set_title('Heston Model Asset Prices')
ax1.set_xlabel('Time')
ax1.set_ylabel('Asset Prices')
plt.show()
