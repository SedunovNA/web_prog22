



# accountr/api/reports.py
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import StreamingResponse
from .. import models, services
router = APIRouter()
@router.post('/import')
def import_csv(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    reports_service: services.ReportsService = Depends(),):
    background_tasks.add_task(        reports_service.import_csv,
        file.file,    )
@router.get('/export')
def export_csv(    reports_service: services.ReportsService = Depends(),
):
    report = reports_service.export_csv()
    return StreamingResponse(
        report,        media_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename=report.csv'},    )