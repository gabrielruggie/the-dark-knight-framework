'''
Loads RegisteredServices.txt file
'''
class ResourceLoader:
    
    REGISTERED_SERVICES = []

    @classmethod
    def load_service_file (cls):
        
        with open('./resources/RegisteredServices.txt', 'r') as service_file:
            services = service_file.readlines()

        for service in services:
            service_fmt = service.strip()
            cls.REGISTERED_SERVICES.append(service_fmt)
