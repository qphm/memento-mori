SELECT * 
FROM suicide 
INNER JOIN happiness ON
suicide.country = happiness.country
INNER JOIN fifa ON
fifa.country = happiness.country
INNER JOIN freedom ON
freedom.country = fifa.country
