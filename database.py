import pymysql
import os


def load_jobs_from_db():
    timeout = 10
    connection = pymysql.connect(
      charset="utf8mb4",
      connect_timeout=timeout,
      cursorclass=pymysql.cursors.DictCursor,
      db="defaultdb",
      host="vs-careers-website-vs-careers-website.f.aivencloud.com",
      password="AVNS_kBRMtMyRi12k0Ep2AGf",
      read_timeout=timeout,
      port=28017,
      user="avnadmin",
      write_timeout=timeout,
    )

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM jobs")
        job = cursor.fetchall()
        jobs = [dict(row) for row in job]

    connection.close()

    return jobs

def load_job_from_db(id):
    timeout = 10
    connection = pymysql.connect(
      charset="utf8mb4",
      connect_timeout=timeout,
      cursorclass=pymysql.cursors.DictCursor,
      db="defaultdb",
      host="vs-careers-website-vs-careers-website.f.aivencloud.com",
      password="AVNS_kBRMtMyRi12k0Ep2AGf",
      read_timeout=timeout,
      port=28017,
      user="avnadmin",
      write_timeout=timeout,
    )

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM jobs WHERE id = %s", (id,))
        job = cursor.fetchone()

    connection.close()

    if job:
        return dict(job)
    else:
        return None

def add_application_to_db(job_id, data):
    timeout = 10
    connection = pymysql.connect(
      charset="utf8mb4",
      connect_timeout=timeout,
      cursorclass=pymysql.cursors.DictCursor,
      db="defaultdb",
      host="vs-careers-website-vs-careers-website.f.aivencloud.com",
      password="AVNS_kBRMtMyRi12k0Ep2AGf",
      read_timeout=timeout,
      port=28017,
      user="avnadmin",
      write_timeout=timeout,
    )

    with connection.cursor() as cursor:
        query = "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (job_id, data['full_name'], data['email'], data['linkedin_url'], data['education'], data['work_experience'], data['resume_url']))

    connection.commit()
    connection.close()