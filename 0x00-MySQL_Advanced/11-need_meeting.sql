CREATE VIEW need_meeting AS
SELECT students.name
FROM students
LEFT JOIN meetings
ON students.id = meetings.student_id
WHERE students.score < 80
AND (meetings.last_meeting IS NULL OR meetings.last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));
