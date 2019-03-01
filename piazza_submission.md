# Team JETLAG: Visualization Submission

## Submitted by: Liuchi Li, Stephanie (Weimeng) Kong, Xiao Tong, Zhicai Zhang

We directly use the solution code for Homework 5 to find the U and V. And then apply SVD on V and get the first two principal conponents of V.

We first try to visualize V[0] and V[1] with a bunch of movies of choices (for example, 10 random movies, 10 mose popular movies, 10 best movies, etc.), but we can not find any clue how to interpret V[0] and V[1].

So instead, we compute the average V[0] and average V[1] for different groups of movies.

The first thing we try is to plot the average V[0] and V[1] for different genres of movies (the plot on the left):

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_averageV_all_generes.png)
![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_random10movies_drama.png)

We find out that the movies on the right side of the plot (V[0]>0) are mostly art movies, for instance documentary and war movies; 
and the movies on the left side (V[0]<0) are commercial movies, such as action and comedy movies.

For V[1], movies with V[1]>0 in general focus on serious topics, such as crime and documentary movies;
while for movies with V[1]<0, the content is more chill, such as children and animation movies.

As an example, we visualize 10 randomly picked drama movies (see the plot on the right above). Clearly, most of them locate at the right side of the plot (V[0]>0).

The next plot we make is the average V[0] and V[1] for different "popularity" of movies (here "popularity" means total number of ratings), below is the plot (the label shows the range of the total number of ratings N_R):

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_averageV_all_num_of_ratings.png)
![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_mostpopular10movies.png)

We can see that the larger V[0] and the smaller V[1], the more popular the movies are, which means that the popular movies are mostly chill and art movies, for example, musical and documentary movies are both art movies, but people prefer musical movies because they are more chill.

Then we also try to plot the average V[0] and V[1] for different "quality" of movies (here "quality" means average ratings of the movie), below is the plot (the label shows the range of the average rating R):

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_averageV_all_ratings.png)

So we clearly see that **the V[0] we get represents the quality of the movie: the better the movie, the larger V[0] is.**

**Conclusion: pupolar and good movies will appear in the bottom-right cornor of our V[0]-V[1] plot, and less-popular and bad movies will appear in the top-left cornor of out plot.**



The END.
