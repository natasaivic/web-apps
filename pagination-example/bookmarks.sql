PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE bookmarks (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  label TEXT NOT NULL, 
  url TEXT NOT NULL, 
  visited INTEGER NOT NULL
);

INSERT INTO bookmarks VALUES(4,'Jinja Templates','https://jinja.palletsprojects.com/en/3.0.x/templates/',0);
INSERT INTO bookmarks VALUES(5,'Flask','https://flask.palletsprojects.com/en/2.0.x/quickstart/#redirects-and-errors',0);
INSERT INTO bookmarks VALUES(6,'The Zen of Python','https://zen-of-python.info/',0);
INSERT INTO bookmarks VALUES(7,'Styling web forms','https://developer.mozilla.org/en-US/docs/Learn/Forms/Styling_web_forms',0);
INSERT INTO bookmarks VALUES(8,'What is a web server?','https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server',0);
INSERT INTO bookmarks VALUES(9,'How do you set up a local testing server?','https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server',0);
INSERT INTO bookmarks VALUES(10,'Document and website structure','https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure',0);
INSERT INTO bookmarks VALUES(11,'Client-Server Overview Previous','https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview',0);
INSERT INTO bookmarks VALUES(12,'HTTP response status codes','https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses',0);
INSERT INTO bookmarks VALUES(13,'PyTouch','https://github.com/facebookresearch/PyTouch',0);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('bookmarks',13);
COMMIT;
