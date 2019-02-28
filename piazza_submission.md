Team JETLAG: visualization submission

Submitted by: Liuchi Li, Stephanie (Weimeng) Kong, Xiao Tong, Zhicai Zhang

We directly use the solution code for Homework 5 to find the U and V. And then apply SVD on V and get the first two principal conponents of V.

we first tried to visualize V[0] and V[1] with a bunch of movies of choices (10 random movies, 10 mose popular movies, 10 best movies, etc.), but we could not find any clue how to interplate V[0] and V[1] (probably due to our lack of knowledge of the movies?).

So instead, we try to get the average V[0] and average V[1] for different groups of movies.

The first thing we tried is to plot the average V[0] and V[1] for different "quality" of movies (here "quality" means average ratings of the movie), below is the plot:

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_bias_mostpopular10movies.png)

