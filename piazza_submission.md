# Team JETLAG: Visualization Submission

## Submitted by: Liuchi Li, Stephanie (Weimeng) Kong, Xiao Tong, Zhicai Zhang

We directly use the solution code for Homework 5 to find the U and V. And then apply SVD on V and get the first two principal conponents of V.

We first try to visualize V[0] and V[1] with a bunch of movies of choices (for example, 10 random movies, 10 mose popular movies, 10 best movies, etc.), but we can not find any clue how to interpret V[0] and V[1].

So instead, we compute the average V[0] and average V[1] for different groups of movies.

The first thing we try is to plot the average V[0] and V[1] for different genres of movies (the plot on the left):

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_averageV_all_generes.png)
![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_random10movies_drama.png)

We find out that the movies on the right side of the plot (V[0]>0) are mostly classy and sophisticated, for instance documentary and war movies; 
and the movies on the left side (V[0]<0) are commercial movies, such as action and comedy movies.

For V[1], movies with V[1]>0 in general focus on serious topics, such as crime and documentary movies;
while for movies with V[1]<0, the content is more chill, such as children and animation movies.

As an example, we visualize 10 randomly picked drama movies (see the plot on the right above). Clearly, most of them locate at the right side of the plot (V[0]>0).

The next plot we make is the average V[0] and V[1] for different "popularity" of movies (here "popularity" means total number of ratings), below is the plot (the label shows the range of the total number of ratings N_R), see the left plot below:

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_averageV_all_num_of_ratings.png)
![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_mostpopular10movies.png)

We can see that the larger V[0] and the smaller V[1], the more popular the movies are, which means that the popular movies are mostly chill (small V[1]), classy and sophisticated (large V[0]), for example, musical and documentary movies are both classy and sophisticated, but people prefer musical movies because they are more chill. However, we observe one exception, which is very popular (420 < NR < 480) but has small V[0] (corresponding to commercial movies); this is understandable because many people watch those blockbusters.

For instance, we visualize the 10 most popular movies (see the plot on the right above). As we can see, all of them are in the V[1]<0 region, and the majority (60%) of them have V[0] > 0. But there are also movies in V[0] <0 region, for example, the movie "Independence Day" - a classic blockbuster.

Lastly, we visualize movies in terms of their average ratings. The plot below shows the average V[0] and V[1] for different average ratings of the movie:

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/visualize_V_averageV_all_ratings.png)

There is a clear trend that people prefer more classy and sophisticated (large V[0]), and more chill (small V[1]) movies.

