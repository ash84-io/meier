import pymysql
from datetime import datetime
import re
from bs4 import BeautifulSoup
import os


def clean_html_content(content):
    """HTML 또는 마크다운 컨텐츠를 플레인 텍스트로 변환"""
    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(content, "html.parser")

    # 스크립트와 스타일 태그 제거
    for script in soup(["script", "style"]):
        script.decompose()

    # HTML을 텍스트로 변환
    text = soup.get_text(separator=" ")

    # 불필요한 공백과 빈 줄 정리
    text = re.sub(r"\n\s*\n", "\n\n", text.strip())
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_and_save_content():
    # 데이터베이스 연결 설정
    db_config = {
        "host": os.environ.get("DB_HOST").split(":")[0],
        "port": int(os.environ.get("DB_HOST").split(":")[1]),
        "user": os.environ.get("DB_USER"),
        "password": os.environ.get("DB_PASSWORD"),
        "db": os.environ.get("DB_NAME"),
    }

    print(db_config)

    try:
        # 데이터베이스 연결
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()

        # 현재 날짜로 파일명 생성
        today = datetime.now().strftime("%Y%m%d")
        output_file = f"knowledge-{today}.txt"

        # post 테이블에서 데이터 조회
        query = "SELECT title, content FROM post WHERE content IS NOT NULL AND in_date >= '2018-01-01 00:00:00'"
        cursor.execute(query)

        # 결과를 파일에 작성
        with open(output_file, "w", encoding="utf-8") as f:
            for title, content in cursor:
                if content:
                    # 컨텐츠 정제
                    # 마크다운 이미지 문법 제거 후 HTML 정제
                    content = re.sub(
                        r"!\[.*?\]\(.*?\)", "", content
                    )  # ![alt](url) 형식 제거
                    content = re.sub(r"<img.*?>", "", content)  # <img> 태그 제거
                    clean_content = clean_html_content(content)

                    # 파일에 작성
                    f.write(f"Title: {title}\n")
                    f.write(f"Content: {clean_content}\n")
                    f.write("\n===\n")

        print(f"Content has been extracted and saved to {output_file}")

    except pymysql.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if "conn" in locals():
            cursor.close()
            conn.close()


if __name__ == "__main__":
    extract_and_save_content()
