# Team JETLAG: Visualization sVubmission

## Submitted by: Liuchi Li, Stephanie (Weimeng) Kong, Xiao Tong, Zhicai Zhang

We directly use the solution code for Homework 5 to find the U and V. And then apply SVD on V and get the first two principal conponents of V.

we first tried to visualize V[0] and V[1] with a bunch of movies of choices (10 random movies, 10 mose popular movies, 10 best movies, etc.), but we could not find any clue how to interplate V[0] and V[1] (probably due to our lack of knowledge of the movies?).

So instead, we try to get the average V[0] and average V[1] for different groups of movies.

The first thing we tried is to plot the average V[0] and V[1] for different "quality" of movies (here "quality" means average ratings of the movie), below is the plot (the label shows the range of the average rating R):

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_averageV_all_ratings.png)

So we clearly see that the V[0] we get represents the quality of the movie: the better the movie, the smaller V[0] is.

The next thing we tried is to plot the average V[0] and V[1] for different "popularity" of movies (here "popularity" means total number of ratings), below is the plot (the label shows the range of the total number of ratings N_R):

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_averageV_all_num_of_ratings.png)

Surprisingly, we also see that the V[1] we get represents now the popularity of the movie: the more popular the movie, the smaller V[1] is.

As a conclusion: pupolar and good movies will appear in the left-bottom cornor of our V[0]-V[1] plot, and less-popular and bad movies will appear in the top-right cornor of out plot.

To verify this, we choose ten random movies, and plot their V[0] and V[1], and the numbers in the braket after the name of the movie means (NR, R), where NR is the number of ratings to that movie, and R is the average rating of that movie:

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_random10movies.png)

We see that the rule we observe above is basically correct:  pupolar and good movies will appear in the left-bottom cornor of our V[0]-V[1] plot, and less-popular and bad movies will appear in the top-right cornor of out plot.

And some other verification: we plot the ten most popular movies -  not surprisingly, they all appear at the bottom of the plot:

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_mostpopular10movies.png)


And we also plot the best 10 movies - which all sit in the left side of the plot:

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_best10movies.png)

The END.
