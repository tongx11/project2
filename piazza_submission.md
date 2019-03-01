# Team JETLAG: Visualization Submission

## Submitted by: Liuchi Li, Stephanie (Weimeng) Kong, Xiao Tong, Zhicai Zhang

We directly use the solution code for Homework 5 to find the U and V. And then apply SVD on V and get the first two principal conponents of V.

We first try to visualize V[0] and V[1] with a bunch of movies of choices (for example, 10 random movies, 10 mose popular movies, 10 best movies, etc.), but we can not find any clue how to interplate V[0] and V[1] (probably due to our lack of knowledge of the movies?).

So instead, we try to get the average V[0] and average V[1] for different groups of movies.

The first thing we try is to plot the average V[0] and V[1] for different genres of movies:

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_averageV_all_generes.png)
![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_random10movies_drama.png)

The next thing we try is to plot the average V[0] and V[1] for different "popularity" of movies (here "popularity" means total number of ratings), below is the plot (the label shows the range of the total number of ratings N_R):

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_averageV_all_num_of_ratings.png)
![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_mostpopular10movies.png)

Surprisingly, we also see that **the V[1] we get represents the popularity of the movie: the more popular the movie, the smaller V[1] is.**

Then we also try to plot the average V[0] and V[1] for different "quality" of movies (here "quality" means average ratings of the movie), below is the plot (the label shows the range of the average rating R):

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_averageV_all_ratings.png)

So we clearly see that **the V[0] we get represents the quality of the movie: the better the movie, the larger V[0] is.**

**Conclusion: pupolar and good movies will appear in the bottom-right cornor of our V[0]-V[1] plot, and less-popular and bad movies will appear in the top-left cornor of out plot.**



The END.
