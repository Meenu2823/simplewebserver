from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <style>
        .icon {
            color: #cc324b;
            font-size: 25px;
            padding: 5px;
        }

        i:hover {
            color: gray;
        }

        .menu {
            color: #cc324b;
            font-size: 15px;
            padding: 5px;
        }

        a:hover {
            color: gray;
        }

        .bgc {
            background-color: lightgrey;
        }
    </style>
</head>

<body style="background-color: #cc324b;">
    <div class="row border border-3 bgc">
        <div class="col-4 bgc">
            <i class="bi bi-twitter icon"></i>
            <i class="bi bi-youtubr icon"></i>
            <i class="bi bi-linkedin icon"></i>
            <i class="bi bi-pinterest icon"></i>
            <i class="bi bi-facebook icon"></i>
            <i class="bi bi-whatsapp icon"></i>
            <i class="bi bi-instagram icon"></i>
        </div>
        <div class="col-5 bgc">
            <nav class="navbar navbar-expand-lg bgc">
                <div class="container-fluid">
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                        data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false"
                        aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNavDropdown">
                        <ul class="navbar-nav">
                            <li class="nav-item">
                                <a class="nav-link  menu" aria-current="page" href="#">Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link menu" href="#">Alumini</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link menu" href="#">Events</a>
                            </li>
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle menu" href="#" role="button"
                                    data-bs-toggle="dropdown" aria-expanded="false">
                                    Departments
                                </a>
                                <ul class="dropdown-menu">
                                    <li><a class="dropdown-item menu" href="#">Computer Science Engineering</a></li>
                                    <li><a class="dropdown-item menu" href="#">Artificial Intelligence & Data
                                            Science</a></li>
                                    <li><a class="dropdown-item menu" href="#">EEE</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
        <div class="col-3 bgc">
            <div class="border border-3 border-dark rounded-5">
                <i class="bi bi-search icon"></i>

                <input type="text" class="bgc border-0" />

            </div>
        </div>
    </div>
    <h6 style="color: beige;">University Toppers</h6>
    <table class="table table-success table-striped">
        <tr>
            <th>REG.NO</th>
            <th>NAME</th>
            <th>BRANCH</th>
        </tr>
        <tr>
            <td>101</td>
            <td>Arjun</td>
            <td>CSE</td>
        </tr>
        <tr>
            <td>102</td>
            <td>Geetha</td>
            <td>AI&DS</td>
        </tr>
        <tr>
            <td>103</td>
            <td>Soundharya</td>
            <td>B.Des</td>
        </tr>
        <tr>
            <td>104</td>
            <td>Pavithra</td>
            <td>CSE.IoT</td>
        </tr>
    </table>

        <div style="width: 100%;">
            <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
                <div class="carousel-indicators">
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0"
                        class="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"
                        aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"
                        aria-label="Slide 3"></button>
                </div>
                <div class="carousel-inner">
                    <div class="carousel-item active" data-bs-interval="2000">
                        <img src="img1.jpg" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item" data-bs-interval="1500">
                        <img src="img2.jpg" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item" data-bs-interval="500">
                        <img src="img4.jpg" class="d-block w-100" alt="...">
                    </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
                    data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
                    data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
        </div>

    
        

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</body>

</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type','text/html;charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address=('',8000)
httpd=HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()