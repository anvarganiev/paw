COPY programers_skill
FROM '/home/omnuse/Projects/paw/datadump/skills'
DELIMITER ','
CSV;

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