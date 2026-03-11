class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response=get_response
        
    def __call__(self,request):
        print(f"Request to:{request.path}")
        response=self.get_response(request)

        response ['X-Custom-Header']='Added by middleware'
        return response
