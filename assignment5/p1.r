raw_data <- read.csv(file = "seaflow_21min.csv", header = TRUE, sep = ",");
library(caret);
set.seed(1234);
trainIndex <- createDataPartition(raw_data$pop, p = .5,
                                  list = FALSE,
                                  times = 1);
trainPart <- raw_data[trainIndex,];
testPart <- raw_data[-trainIndex,];
# plot pe vs chl_small
library(ggplot2)
qplot( raw_data$chl_small, raw_data$pe, color = raw_data$pop);
library(rpart)
fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
model <- rpart(fol, method="class", data = trainPart);
predicted_label <- predict(model, testPart, type = "class");
accuracy = sum(predicted_label == testPart$pop)/dim(testPart)[1];

# build random forest
library(randomforest)
model <- randomForest(fol, data=trainPart);
predicted_forest = predict(model, testPart, type = "class");
accuracy_forest = sum(predicted_forest == testPart$pop)/dim(testPart)[1];

# SVM
library(e1071)
model3 <- svm(fol, data=trainPart);
predicted_svm = predict(model, testPart, type = "class");
accuracy_svm = sum(predicted_svm == testPart$pop)/dim(testPart)[1];

# construct confusion matrix
table(pred = predicted_svm, true = testingdata$pop);

# remove data with fileid 208
qplot( raw_data$time, raw_data$chl_big, color = raw_data$pop);
clean_data = raw_data[which(raw_data$file_id != 208),];

## sample the clean data
set.seed(1457);
trainIndex <- createDataPartition(clean_data$pop, p = .5,
                                  list = FALSE,
                                  times = 1);
trainPart <- clean_data[trainIndex,];
testPart <- clean_data[-trainIndex,];

## decision tree
fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
model1 <- rpart(fol, method="class", data = trainPart);
predicted_label <- predict(model1, testPart, type = "class");
accuracy_tree = sum(predicted_label == testPart$pop)/dim(testPart)[1];

## svm 
model3 <- svm(fol, data=trainPart);
predicted_svm = predict(model, testPart, type = "class");
accuracy_svm = sum(predicted_svm == testPart$pop)/dim(testPart)[1];

## random forest


