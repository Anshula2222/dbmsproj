CREATE TABLE User
(
  Fname INT NOT NULL,
  Lname INT NOT NULL,
  Mail VARCHAR(30) NOT NULL,
  Gender VARCHAR(1) NOT NULL,
  Age INT NOT NULL,
  Uname INT NOT NULL,
  PRIMARY KEY (Uname)
);

CREATE TABLE Preference
(
  Uname INT NOT NULL,
  Gender VARCHAR(1) NOT NULL,
  Age INT NOT NULL,
  Height INT NOT NULL,
  Religion VARCHAR(30) NOT NULL,
  Job VARCHAR(30) NOT NULL,
  Nationality VARCHAR(30) NOT NULL,
  Mothertongue VARCHAR(15) NOT NULL,
  PRIMARY KEY (Uname),
  FOREIGN KEY(Uname) REFERENCES User(Uname) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Profile
(
  Uname INT NOT NULL,
  Gender VARCHAR(1) NOT NULL,
  Age INT NOT NULL,
  Height INT NOT NULL,
  Religion VARCHAR(30) NOT NULL,
  Job VARCHAR(30) NOT NULL,
  Bio VARCHAR(50),
  Nationality VARCHAR(15) NOT NULL,
  Mothertongue VARCHAR(15) NOT NULL,
  PRIMARY KEY (Uname),
  FOREIGN KEY(Uname) REFERENCES User(Uname) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Photos
(
  Pid INT NOT NULL,
  Uname INT NOT NULL,
  PRIMARY KEY (Pid),
  FOREIGN KEY(Uname) REFERENCES User(Uname) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Feedback
(
  Uname INT NOT NULL,
  Feedback INT NOT NULL,
  F_text VARCHAR(30),
  PRIMARY KEY (Uname),
  FOREIGN KEY(Uname) REFERENCES User(Uname) ON DELETE CASCADE ON UPDATE CASCADE
);