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
1) n = 7
2) Portfolio = create_portfolio(n)
3) Mean_portfolio = create_portfolio_mean(Portfolio)
4) Z = create_correlated_GBMs(n)
5) dataset = create_dataset(Z)
6) principal_breast_Df = fast_PCA(dataset, n_components = 3)
7) T = 1.0                
8) N = 10000               
9) M = 1
10) fig, ax1  = plt.subplots(1, 1, figsize=(12,5))
11) time = np.linspace(0,T,N+1)
12) Means_pca = []
13) for j in range(principal_breast_Df.shape[1]):
14)  S = heston_model_sim2(Mean_portfolio[0], Mean_portfolio[3], Mean_portfolio[1], Mean_portfolio[2], Mean_portfolio[4],T, N, M, Z, ind = j, principal_breast_Df = 15)principal_breast_Df[str(j)])
16)  Means_pca.append(S.mean())
17)  ax1.plot(time,S,label = '{}instrument'.format(j))

18) ax1.set_title('Heston Model Asset Prices')
19) ax1.set_xlabel('Time')
20) ax1.set_ylabel('Asset Prices')
21) plt.show()

21) For Basic Monte Carlo simulations:
22) fig, ax1  = plt.subplots(1, 1, figsize=(12,5))
23) time = np.linspace(0,T,N+1)
24) Means = []
25) for i in range(len(Portfolio)):
26)  S = heston_model_sim(S0 = Portfolio[i][0], v0 = Portfolio[i][3], kappa = Portfolio[i][1], theta = Portfolio[i][2], sigma = Portfolio[i][4],T=T, N=N, M=M, Z=Z, ind = i)
27)  Means.append(S.mean())
28)  ax1.plot(time,S,label = '{}instrument'.format(i))

ax1.set_title('Heston Model Asset Prices')
ax1.set_xlabel('Time')
ax1.set_ylabel('Asset Prices')
plt.show()
