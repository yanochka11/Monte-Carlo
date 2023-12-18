# Monte-Carlo
In the realm of finance, our research addresses the challenge to speed up Monte Carlo simulations without significant loss in accuracy.   Experimental results aim to validate this hypothesis, offering insights to enhance investment strategies.
We prepared both py and ipynb versions. If someone wants to check results of experiments then open ipynb version with ready to watch plots, if someone want to start testing out solution you are free to use py version. 

Our solution proposes 4 steps:
1. Generate an n asset portfolio.
2. Generate GBM random correlated motions for each asset.
3. Use PCA to decrease the dimension of GBM's motions matrix
4. Use Monte Carlo to simulate processes.

Links to papers and guides that helped us:
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4066115
https://sas.uwaterloo.ca/~dlmcleis/s906/chapt1-6.pdf
https://www.informs-sim.org/wsc07papers/107.pdf
https://arxiv.org/pdf/1903.10795v1.pdf
https://www.youtube.com/watch?v=o8C6DxZh8dw
