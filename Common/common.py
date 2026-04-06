import socket

def getLocalIP():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sc:
            return  sc.getsockname()[0]
        
    except Exception as e:    
        return "127.0.0.1" # 실패 시 루프백 반환
    
    finally:
        sc.close()

