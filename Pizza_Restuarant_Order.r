order_pizza <- function(){
t_foods <-c("Pizza","Appetizers","Spaghetti")
df_pizza <- data.frame(size_pizza = c("L","M","S"),cost_p = c(359,259,159))
crust_pizza <- c("Thin","Pan")
pizza1 <- c("Seafood Cocktail","Double Cheese","Hawaiian","Super Deluxe","Tom Yam Kung")
df_appe <- data.frame(appe = c("Korean Chic","BBQ Chic","Garlic Bread","French Fires"),cost_ap = c(159,129,79,89))
df_sph <- data.frame(sph = c("Carbonara","Pork Bologness","Keemao Sausage"),cost_sp = c(169,169,139))
cost <- 0
piz_n <- 0
app_n <- 0
sph_n <- 0
count <- 0
time <- 15
run <- TRUE
order_ag <- "Y"
print("Welcome to My Pizza Restuarant")
print("What's category of food do you want to order?")
print(t_foods)
while(run == TRUE){
  if(count>0){
    print("Would you like to order more items? (Y,N)")
    order_ag <- readLines("stdin",n=1)
    if(order_ag == "N"){break}
    if(order_ag != "Y"){print("Invalid data, please order again!")}else{print(t_foods)}
  }
  if(order_ag == "Y"){
    kind_foods <- readLines("stdin",n=1)
    if(kind_foods=="Pizza"){
      print("Choose Size(L,M,S): ")
      size_pz <- readLines("stdin",n=1)
      i <- size_pz == df_pizza$size_pizza[]
      if(sum(i)==0){
        print("Incorrect Items, please order again!") 
        cost <- cost + 0
      }else{cost <- cost + (df_pizza$cost_p[i])
        piz_n <- piz_n + 1
        print("Choose Crust(Thin,Pan): ")
        crust_pz <- readLines("stdin",n=1)
        print(pizza1)
        print("Choose Pizza: ")
        pz <- readLines("stdin",n=1)} 
    }
    else if(kind_foods=="Appetizers"){
      print("Menu if Appetizers")
      print(df_appe[1:4,])
      print("Choose Appetizers: ")
      ap <- readLines("stdin",n=1)
      j <- ap == df_appe$appe[]
      if(sum(j)!=0){
        cost <- cost + (df_appe$cost_ap[j])
        app_n <- app_n + 1
      }else{print("Incorrect Items, please order again!")
        cost <- cost + 0}  
    }else if(kind_foods=="Spaghetti"){
      print("Menu if Spaghetti")
      print(df_sph[1:3,])
      print("Choose Spaghetti: ")
      sp <- readLines("stdin",n=1)
      k <- sp == df_sph$sph[]
      if(sum(k)!=0){
        cost <- cost + (df_sph$cost_sp[k])
        sph_n <- sph_n + 1
      }else{print("Incorrect Items, please order again!")
        cost <- cost + 0}
    }
      if(order_ag == "N"){break}
    }
    count <- count + 1
  }
print("Do you want to confirm order? (CF CC)")
order_cf <- readLines("stdin",n=1)
if(order_cf == "CC"){print("Cancel orders successfully, thank you :]")}else{
  print(paste("Total order of pizza is",piz_n,"pcs."))
  print(paste("Total order of appetizer is",app_n,"pcs."))          
  print(paste("Total order of spaghetti is",sph_n,"pcs."))
  time <- (piz_n + app_n + sph_n)*time
  print(paste("Total amount order is ",cost," THB. Thank you for your order,  please wait about",time," minutes."))
  }
}
order_pizza()