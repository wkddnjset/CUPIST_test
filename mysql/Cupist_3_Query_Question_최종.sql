/*********************************************/
-- 3, 데이터베이스 생성 및 테이블 생성 
/*********************************************/

-- 데이터베이스 생성
CREATE DATABASE Cupist; 

-- 사용자 테이블 생성
CREATE TABLE Cupist.users (
	id INT PRIMARY KEY AUTO_INCREMENT, 
    nickname VARCHAR(50), 		-- 닉네임 
    sex INT, 					-- 성별 
    birthdate DATE 				-- 생일 
);
    
-- 관심사 테이블 생성
CREATE TABLE Cupist.interest (
	id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT, 				-- 사용자 인덱스 
    interest VARCHAR(100), 		-- 관심사 
	FOREIGN KEY (user_id) REFERENCES users (id)
);

-- 좋야요 기록 테이블 생성
CREATE TABLE Cupist.heart (
	send_user_id INT , 		-- 좋아요를 보낸 사용자의 인덱스 
    receive_user_id INT , 	-- 좋아요를 받은 사용자의 인덱스
    PRIMARY KEY (send_user_id, receive_user_id),
	FOREIGN KEY (send_user_id) REFERENCES users (id),
    FOREIGN KEY (receive_user_id) REFERENCES users (id)
);

-- 대화 내용 저장 테이블 생성
CREATE TABLE Cupist.chat_log (
	female_user_id INT, 		-- 여성 사용자의 인덱스 
    male_user_id INT, 			-- 남성 사용자의 인덱스 
    status_flag INT, 			-- 대화창의 상태
    insert_date DATETIME, 		-- 로그가 기록될 시간
    PRIMARY KEY (female_user_id, male_user_id),
	FOREIGN KEY (female_user_id) REFERENCES users (id),
    FOREIGN KEY (male_user_id) REFERENCES users (id)
);

/*********************************************/
-- 4. 쿼리 작성
/*********************************************/

/*
	사용자 A : A
    사용자 B : B
    
    조건
    - sex -> 0 : 남자  1 : 여자
    - chat_log.status_flag -> 0 : 대화 종료 1: 대화 중
*/
SET @userAid = (SELECT id FROM Cupist.users WHERE nickname = 'A');
SET @userBid = (SELECT id FROM Cupist.users WHERE nickname = 'B');

-- a. 사용자 A가 사용자 B에게 좋아요를 보냈는지 여부
SELECT 
	IF( COUNT(*) = 0, '싫어요', '좋아요 ' ) AS '좋아요 여부'
FROM
	Cupist.heart AS h
WHERE 
	h.send_user_id = @userAid
AND
    h.receive_user_id = @userBid ;
    
-- b. 사용자 A가 사용자 B에게 연결되었는지 여부
-- self join
SELECT
	IF (heart_send.send_user_id = heart_receive.receive_user_id ,'연결','연결 안됨') AS '결과'
FROM
	Cupist.heart AS heart_send,
    Cupist.heart AS heart_receive
WHERE
	heart_send.receive_user_id = heart_receive.send_user_id
AND
	heart_send.send_user_id = @userAid
 AND
	heart_send.receive_user_id = @userBid ;
    
-- c. 사용자 A가 접속중인 대화방의 정보
-- if문 으로 여성인지 남성인지 판단한 이후에 대화방의 정보를 가져옴
SELECT 
	(SELECT nickname FROM Cupist.users WHERE id = cl.female_user_id) AS '여성 대화 상대',
	(SELECT nickname FROM Cupist.users WHERE id = cl.male_user_id) AS ' 남성 대화 상대',
	(CASE cl.status_flag
		WHEN 0 THEN '종료된 대화입니다.'
		WHEN 1 THEN '진행중인 대화입니다.'
		ELSE '상태값이 올바르지 않습니다.'
		END
	) AS '대화 상태',
    cl.insert_date AS '로그 기록 시간'
FROM Cupist.chat_log as cl WHERE 
IF ((SELECT sex FROM Cupist.users WHERE nickname = 'A' )= 0,(cl.male_user_id = @userAid ),(cl.female_user_id = @userAid ));

-- d. 사용자 A의 프로필 정보
 -- 프로필 정보 가져오기 
SELECT
	nickname AS '닉네임',
    IF (sex=0, '남자', '여자') AS '성별',
    birthdate AS '생일'
FROM 
	Cupist.users
WHERE 
	id = @userAid;
    
 -- 관심사 정보 가져오기
SELECT interest FROM Cupist.interest WHERE user_id = @userAid;
        
-- e. 사용자 A를 좋아요한 사람들의 정보
SELECT * FROM Cupist.users
WHERE id in (SELECT send_user_id FROM Cupist.heart WHERE receive_user_id = @userAid);