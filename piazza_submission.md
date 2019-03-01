# Team JETLAG: Visualization Submission

## Submitted by: Liuchi Li, Stephanie (Weimeng) Kong, Xiao Tong, Zhicai Zhang

We directly use the solution code for Homework 5 to find the U and V, and then apply SVD on V and get the first two principal components of V.

We first try to visualize V[0] and V[1] with a bunch of movies of choices (for example, 10 random movies, 10 mose popular movies, 10 best movies, etc.), but we can not find any clue how to interpret V[0] and V[1].

So instead, we compute the average V[0] and average V[1] for different groups of movies.

The first thing we try is to plot the average V[0] and V[1] for different genres of movies (the plot on the left):

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/piazza/fig1.png)

We find out that the movies on the right side of the plot (V[0]>0) are mostly classy and sophisticated with great storylines, for instance documentary and war movies; 
and the movies on the left side (V[0]<0) are commercial movies, such as action and comedy movies.

For V[1], movies with V[1]>0 in general focus on serious topics, such as crime and documentary movies;
while for movies with V[1]<0, the content is more cheering and relaxing, such as children and animation movies.

As an example, we visualize 10 randomly picked drama movies (see the plot on the right above). Clearly, most of them locate on the right side of the plot (V[0]>0). One thing to note that, Gone with the wind, which is the signature classical romance movie, is also present on this plot, which fit the described V[0] V[1] trend fairly well.

The next plot we make is the average V[0] and V[1] for different "popularity" of movies (here "popularity" means total number of ratings), below is the plot (the label shows the range of the total number of ratings N_R), see the left plot below:

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/piazza/fig2.png)

We can see that the larger V[0] and the smaller V[1], the more popular the movies are. It indicates that the popular movies are mostly relaxing (small V[1]) and classy (large V[0]). For example, musical and documentary movies are both classy, but people prefer musical movies because they provide a more cozy atmosphere. However, we observe one exception, which is very popular (420 < NR < 480) but has small V[0] (corresponding to commercial movies); this is understandable because many people watch those blockbusters.

Additonally, we visualize the 10 most popular movies (see the plot on the right above). As we can see, all of them are in the V[1]<0 region, and the majority (60%) of them have V[0] > 0. But there are also movies in V[0] <0 region, for example, the movie "Independence Day" - a classic blockbuster.

Lastly, we visualize movies in terms of their average ratings. The plot below shows the average V[0] and V[1] for different average ratings of the movie:

![alt text](https://github.com/cs155cctw/project2/blob/master/plots/piazza/fig3.png)

There is a clear trend that people prefer more classy and sophisticated (large V[0]), and more cozy (small V[1]) movies.

On Netflix, from a quick Google search, the number of active female subscribers are more than males. This also explains the trend we observe previously since female audience are geared to watch movies in 
