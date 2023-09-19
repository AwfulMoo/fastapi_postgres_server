<a name="readme-top"></a>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">fastapi_postgres_server</h3>

  <p align="center">
    Template for a simple python FastAPI connecting to postgres 
    <br />
    <br />
    <a href="https://github.com/AwfulMoo/fastapi_postgres_server/issues">Report Bug</a>
    ·
    <a href="https://github.com/AwfulMoo/fastapi_postgres_server/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a blank template for a Python based asynchronous API. This project makes use of FastAPI, SQLAlchemy and features Rich logging.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![FastAPI][FastAPI.tiangolo.com]][FastAPI-url]
* [![SQLAlchemy][SQLAlchemy.org]][SQLAlchemy-url]
* [![Rich][Rich.readthedocs.io]][Rich-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

I'd recommend using Poetry to manage the dependecy installation/ virtual environment setup.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Poetry
  ```sh
  curl -sSL https://install.python-poetry.org | python3 -
  ```
* PostgreSQL  
  See the [the download page](https://www.postgresql.org/download/) or the [docker image](https://hub.docker.com/_/postgres)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AwfulMoo/fastapi_postgres_server.git
   ```
2. Install Python packages (from inside the cloned repo)
   ```sh
   poetry install
   ```
3. Select the Python intpreter (use the path to the poetry virtual env created in the last step)
   ```sh
   poetry install
   ```
4. Update the config.py file to include database connection settings as needed

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Edit and expand on the application as needed.

You can debug the application by pressing *F5* in [Visual Studio Code](https://code.visualstudio.com/) 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/AwfulMoo/fastapi_postgres_server](https://github.com/AwfulMoo/fastapi_postgres_server)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AwfulMoo/fastapi_postgres_server.svg?style=for-the-badge
[contributors-url]: https://github.com/AwfulMoo/fastapi_postgres_server/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AwfulMoo/fastapi_postgres_server.svg?style=for-the-badge
[forks-url]: https://github.com/AwfulMoo/fastapi_postgres_server/network/members
[stars-shield]: https://img.shields.io/github/stars/AwfulMoo/fastapi_postgres_server.svg?style=for-the-badge
[stars-url]: https://github.com/AwfulMoo/fastapi_postgres_server/stargazers
[issues-shield]: https://img.shields.io/github/issues/AwfulMoo/fastapi_postgres_server.svg?style=for-the-badge
[issues-url]: https://github.com/AwfulMoo/fastapi_postgres_server/issues
[license-shield]: https://img.shields.io/badge/LICENSE-MIT-yellow?style=for-the-badge
[license-url]: https://github.com/AwfulMoo/fastapi_postgres_server/blob/master/LICENSE
[SQLAlchemy.org]: https://img.shields.io/badge/SQLAlchemy-778777.svg?style=for-the-badge&logo=data:image/svg%2bxml;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAAAABMLAAATCwAAAAAAAAAAAAB3iHf/d4h3/3eId/93iHf/d4h3/3eId/93iHf/d4h3/3eId/93iHf/d4h3/3eId/93iHf/d4h3/3eId/93iHf/d4h3/3eId/93iHf/d4h3/3eId/93iHf/d4h3/3eId/93iHf/d4h3/3eId/93iHf/d4h3/3eId/93iHf/d4h3/3eId/93iHf/d4h3/3eId/95inn/lKGU/77Hvv/R1tH/0NXQ/8XMxf+hraH/eot6/3eId/93iHf/d4h3/3eId/93iHf/d4h3/3eId/94iXj/uMG4//T29P/29/b/6+7r/+zv7P/8/fz//f79/8TLxP+QnZD/d4h3/3eId/93iHf/d4h3/3eId/95inn/uMC4//r7+v/N1M3/l6SX/4CQgP+Ek4T/naqd/9DW0P/7/Pv/5Ofk/4mYif93iHf/d4h3/3eId/93iHf/rrmu//39/f/FzMX/e4x7/3eId/+Il4j/i5qL/3eId/95iXn/tL20//3+/f/Hzsf/e4x7/3eId/93iHf/f49//+Hk4f/i5uL/gZCB/3eId/+wubD/7vDu//Dx8P+8xbz/fY19/3yNfP/T2NP/+fr5/56qnv93iHf/d4h3/5Gekf/x8vH/ucG5/3eId/+msab/7/Hv/8zSzP/L0sv/+fn5/7bAtv93iHf/q7ar//////+9xr3/d4h3/3eId/+ap5r/8/Tz/6SwpP9/j3//5unm/+Dk4P95iXn/d4h3/9ne2f/d4t3/fo5+/56qnv/8/fz/yM7I/3eId/93iHf/m6eb//n5+f+st6z/eIl4/9DW0P/z9PP/laKV/4uai//p6+n/0dbR/3mJef+iraL//f79/8bNxv93iHf/d4h3/4qYiv/o6+j/xs3G/3eId/+eqp7/8/Xz//Dx8P/u8O7/8/Xz/6CsoP93iHf/wcnB//7//v+4wLj/eYp5/3eId/95inn/vsa+//Hz8f+cqJz/d4h3/5ikmP/Gzcb/xc3F/5qmmv93iHf/k6CT//Dx8P/r7uv/kJ6Q/3iJeP93iHf/d4h3/4CPgP/c4dz/8/Xz/623rf94iHj/d4h3/3eId/93iHf/prGm/+vt6//8/fz/r7mv/3iIeP93iHf/d4h3/3eId/93iHf/maaZ/+Hl4f/5+vn/1drV/7K7sv+yvLL/0NXQ//z8/P/+//7/vMW8/3iJeP93iHf/d4h3/3eId/93iHf/d4h3/3eId/+CkoL/ucG5/+ns6f/29/b/+Pn4/+vt6//O1M7/qbOp/3uMe/93iHf/d4h3/3eId/93iHf/d4h3/3eId/93iHf/d4h3/3eId/+FlIX/lqSW/5mmmf+Hlof/eIl4/3eId/93iHf/d4h3/3eId/93iHf/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==
[SQLAlchemy-url]: https://www.sqlalchemy.org/
[FastAPI.tiangolo.com]: https://img.shields.io/badge/FastAPI-grey?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/
[Rich.readthedocs.io]: https://img.shields.io/badge/Rich-5868de.svg?style=for-the-badge&logo=data:image/svg%2bxml;base64,AAABAAEAHh4QAAEABADAAgAAFgAAACgAAAAeAAAAPAAAAAEABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABRgaAD0XEAACLS0AayofAIwrFwC6OxwAA0JCAJ1HOwACWVoAyF1LAARsbQDdaFoABYaGAAKkowAOwcEAzMzMzMzMzMzMzMzMzMzMAMyqqqqqqqqqqqqqqqrMzADKQgAAAAAAAAAAAAACTMwAwp50Zlvu/u/u7+41ZiTMAKD/NWZd////////4VZgrACg79cSfv////////6SIswAyAm7cAu7u7ubm7u7kQjMAMyoIJu7u7uQRUQLcEiszADMyi3+2+//91Zk3/lMzMwAzMwNskQp//5wHf/9LMzMAMzKgCVmYr7u7u7u0YzMzADMzKQAAAAAAAAAAATMzMwAzMzMR/7gqsqi3v0MzMzMAMzMzIv/0KzMxN/+CszMzADMzMxJsCLMzMLf/gzMzMwAzMykCyUozMzC3/4KzMzMAMyiA9tELMzMxN/+DMzMzADMgd7XBKzMzMJ5vQzMzMwAzKAAAozMzMzC234MzMzMAMzKqqzMzMzMxN2+DMzMzADMzMzMzMzMzMJ3OQzMzMwAzMzMzMzMzMzCC7AMzMzMAMzMzMzMzMzMgN/+CMzMzADMzMzMzMzMyiv//9CszMwAzMzMzMzMzMgef/fjjMzMAMzMzMzMzMzEv/7+94zMzADMzMzMzMzMyg69u+OMzMwAzMzMzMzMzMojF3ESrMzMAMzMzMzMzMzMxEREiszMzADMzMzMzMzMzMzMzMzMzMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
[Rich-url]: https://rich.readthedocs.io/
