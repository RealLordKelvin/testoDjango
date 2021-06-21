from django.core.management.base import BaseCommand

from firstapp.models import FlowFile
from firstapp.management.handler import flow_file_handler

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help = 'type in the name of the flow file here')
    
    def handle(self, *args, **options):
        meters = flow_file_handler.extract_data_items_from_flow_file(options['file_name'])

        for key, value in meters.items():
            if value == '':
                continue
            for i in range(len(value.get('meterId'))):
                try:
                    mpan_core = key
                    meter_id = value['meterId'][i]
                    meter_registration_id = value['meterRegisterId'][i]
                    reading_date_time = value['readingDateTime'][i]
                    reading_register = value['readingRegister'][i]
                    file_name = options['file_name']
                except:
                    continue
            meter = FlowFile(mpan = mpan_core,
                meter_id = meter_id,
                meter_registration_id = meter_registration_id,
                reading_date_time = reading_date_time,
                reading_register = reading_register,
                file_name = file_name)
            meter.save()

            self.stdout.write(self.style.SUCCESS('Added Meter'))


            
        
        

