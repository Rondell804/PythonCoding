import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life.", "https://image.ibb.co/co5Gmm/ToyStory.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#The Toy Story varible provides information about the movie to print the from __init__ function.
#print (toy_story.storyline)



avatar = media.Movie("Avatar", "Aliens from a distant plant must link with humans for survival.", "https://image.ibb.co/hm9Z6m/Avatar.jpg", "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#The Avatar varible provides information about the movie to print the from init function.
#print (avatar.storyline) / This line prints out the 2nd argument within the __init__ function
#avatar.show_trailer()

selma = media.Movie("Selma", "Based on the 1965 Selma to Montgomery voting rights marches.", "https://image.ibb.co/cMreE6/selma.jpg", "https://www.youtube.com/watch?v=RcK3Cazuf84")
#The Selma varible provides information about the movie to print the from init function.
#print (selma.storyline) / This line prints out the 2nd argument within the __init__ function.
#selma.show_trailer() / This line prints out the youtube video from the show_trailer function in Movie class and 4th arg from __init__ function.

friday = media.Movie("Friday", "16 hours in the lives of unemployed Craig Jones (Cube) and Smokey (Tucker).", "https://image.ibb.co/e86qMm/Friday.jpg", "https://www.youtube.com/watch?v=nH1Ulp4PBtA")
#The Friday varible provides information about the movie to print the from init function.
#print (friday.storyline) / This line prints out the 2nd argument within the __init__ function.
#friday.show_trailer() / This line prints out the youtube video from the show_trailer function in Movie class and 4th arg from __init__ function.

movies = [toy_story, avatar, selma, friday]
#The list of movies stored and executed from function open_movies_page imported from fresh_tomatoes file.

fresh_tomatoes.open_movies_page(movies)
#excutes the varible movies and outputs a webpage using the fresh_tomatoes html and python files.
