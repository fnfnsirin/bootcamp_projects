# build a regression model

head(mtcars)

model <- lm(mpg~hp, data= mtcars)

model
