SELECT COUNT(ID) AS FISH_COUNT
FROM FISH_INFO, FISH_NAME_INFO
WHERE FISH_INFO.FISH_TYPE = FISH_NAME_INFO.FISH_TYPE AND (FISH_NAME_INFO.FISH_NAME = "BASS" OR FISH_NAME_INFO.FISH_NAME = "SNAPPER")