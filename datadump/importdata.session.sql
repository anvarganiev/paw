
-- если кто-то что-то сломает в записях в бд, то вот тут есть команды для взятия данных из дампов



COPY programers_skill
FROM '/home/borismarvin/Рабочий стол/paw/datadump/skills'
DELIMITER ','
CSV;

-- .import datadump/skills programers_skill --csv

-- COPY auth_user (
--     password,
--     last_login,
--     is_superuser,
--     username,
--     first_name,
--     last_name,
--     email,
--     is_staff,
--     is_active,
--     date_joined
--   )
-- FROM 'users'
-- DELIMITER ','
-- CSV ;