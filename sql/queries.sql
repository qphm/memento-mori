SELECT
suicide.country,
suicide.suicide_rate,
freedom.freedom_score,
freedom.freedom_rank,
happiness.happiness_rank,
happiness.happiness_score,
fifa.fifa_rank,
fifa.total_points,
fifa.cur_year_avg,
fifa.cur_year_avg_weighted

FROM suicide 
INNER JOIN happiness ON
suicide.country = happiness.country
INNER JOIN fifa ON
fifa.country = happiness.country
INNER JOIN freedom ON
freedom.country = fifa.country
ORDER BY suicide.suicide_rate DESC;
