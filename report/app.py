from flask import render_template
# … your existing imports and setup …

@app.route('/reports')
def view_all_reports():
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT 
              r.report_id,
              u.name      AS patient_name,
              r.doc_type,
              r.report_date,
              r.file_path
            FROM Reports r
            JOIN Users u 
              ON r.patient_id = u.user_id
            ORDER BY r.report_date DESC
        """)
        reports = cursor.fetchall()
    return render_template('view_reports.html', reports=reports)