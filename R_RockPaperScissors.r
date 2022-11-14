minigame <- function(){
count_win_p <- 0
count_win_b <- 0
count_draw <- 0
times <- 0
run <- TRUE
print("Welcome to Rocks-Paper-Scissors")
print("Please enter 'Rocks','Scissors','Paper' for play a game or enter 'end' to finish the game and sum up the score.")
while(run == TRUE){
  game <- c("Rocks","Scissors","Paper")
  print("Player1: ")
  player1 <- readLines("stdin",n=1)
  print(paste("Bot: ",Bot <- sample(game,size =1, replace = TRUE)))
  b <- c(player1, Bot)
  if(player1 == "end"){break}
  if((sum(b %in% game)) != 2){
      print("Enter the wrong word, please try again!")
      }else{
          times <- times + 1  
          if(player1 == Bot){print("Draw!")
              count_draw <- count_draw+1
            }
          if((player1 =="Rocks" & Bot =="Scissors") | (player1 == "Scissors" & Bot =="Paper") | (player1 =="Paper" & Bot =="Rocks")){print("You win!")
              count_win_p <- count_win_p + 1
            }
          if((Bot =="Rocks" & player1 =="Scissors") | (Bot == "Scissors" & player1 =="Paper") | (Bot =="Paper" & player1 =="Rocks")){print("Bot win!")
              count_win_b <- count_win_b + 1 
            }
      }
} 
print(paste("Times of playing(N): ",times))
print(paste("Player wins(n): ",count_win_p))
print(paste("Bot wins(n): ",count_win_b))
print(paste("Draw(n): ",count_draw))
if(times == 0){
  print("N/A")
}else{
  if(times > 0){
  if((count_win_p+count_draw)>(count_win_b+count_draw)){
    print("You win!🥇")
  }else{
  if((count_win_p+count_draw)<(count_win_b+count_draw)){
    print("You lose!🥈")
    }else{print("Draw!")
        }
      }
    }
  }
 }
minigame()

