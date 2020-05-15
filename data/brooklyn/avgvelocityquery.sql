DECLARE startdatetimes, enddatetimes TIMESTAMP;
DECLARE zerolong, zerolat, angle, xdiff, ydiff FLOAT64;

SET startdatetimes = CAST('2014-05-22 18:00:00 America/New_York' AS TIMESTAMP);
SET enddatetimes = CAST('2014-05-23 02:00:00 America/New_York' AS TIMESTAMP);

#bot left lat: 40.626544, long: -74.035065
#bot right lat: 40.588863, long: -73.953972
#top left(approx) lat: 40.734884, long: -73.938376

CREATE TEMP FUNCTION distance(long1 FLOAT64, long2 FLOAT64, lat1 FLOAT64, lat2 FLOAT64) AS 
(SQRT(POW((lat1 - lat2), 2) + POW((long1 - long2), 2)));

SET (zerolong, zerolat) = (-74.035065, 40.626544);

#for clockwise angle rotation
SET angle = ATAN((zerolat - 40.588863)/(-73.953972 - zerolong));

SET xdiff = distance(zerolong, -73.953972, zerolat, 40.588863);

SET ydiff = distance(zerolong, -73.938376, zerolat, 40.734884);

WITH table1 AS (
    SELECT (CAST(TIMESTAMP_DIFF(pickup_datetime, startdatetimes, SECOND) AS FLOAT64) / CAST(60*60 AS FLOAT64)) AS starttimes, 
		(CAST(TIMESTAMP_DIFF(dropoff_datetime, startdatetimes, SECOND) AS FLOAT64) / CAST(60*60 AS FLOAT64)) AS endtimes, 
		(COS(angle) * (pickup_longitude - zerolong) - SIN(angle) * (pickup_latitude - zerolat)) AS startx,
		(SIN(angle) * (pickup_longitude - zerolong) + COS(angle) * (pickup_latitude - zerolat)) AS starty, 
		(COS(angle) * (dropoff_longitude - zerolong) - SIN(angle) * (dropoff_latitude - zerolat)) AS endx, 
		(SIN(angle) * (dropoff_longitude - zerolong) + COS(angle) * (dropoff_latitude - zerolat)) AS endy,
    FROM `nyc-tlc.green.trips_2014`
    WHERE trip_distance > 0.2
		AND trip_distance < 20
  ), table2 AS (
	SELECT starttimes AS times,
		startx, starty, endx, endy,
		distance(startx, endx, starty, endy) / (endtimes - starttimes) AS velocity
	FROM table1
	WHERE
		startx >= 0
		AND starty >= 0
		AND endx >= 0
		AND endy >= 0
		AND startx <= xdiff
		AND starty <= ydiff
		AND endx <= xdiff
		AND endy <= ydiff
    AND endtimes - starttimes > 0.01
  )
SELECT AVG(velocity) AS avgvelocity
FROM table2