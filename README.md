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
[Rich.readthedocs.io]: https://img.shields.io/badge/Rich-748492.svg?style=for-the-badge&logo=data:image/svg%2bxml;base64,iVBORw0KGgoAAAANSUhEUgAAAB8AAAAeCAYAAADU8sWcAAAA0GVYSWZJSSoACAAAAAoAAAEEAAEAAAAfAAAAAQEEAAEAAAAeAAAAAgEDAAMAAACGAAAAEgEDAAEAAAABAAAAGgEFAAEAAACMAAAAGwEFAAEAAACUAAAAKAEDAAEAAAADAAAAMQECAA0AAACcAAAAMgECABQAAACqAAAAaYcEAAEAAAC+AAAAAAAAAAgACAAIAPgAAAAHAAAA+AAAAAcAAABHSU1QIDIuMTAuMzQAADIwMjM6MDk6MTkgMjM6MTc6NDMAAQABoAMAAQAAAAEAAAAAAAAAXEGLPgAAAYVpQ0NQSUNDIHByb2ZpbGUAAHicfZE9SMNAHMVfW6UqLQ6tIOKQoTpZERVx1CoUoUKoFVp1MLn0Q2jSkKS4OAquBQc/FqsOLs66OrgKguAHiKuLk6KLlPi/pNAixoPjfry797h7B/jrZaaaHWOAqllGOpkQsrkVIfiKbkQQxij6JGbqs6KYguf4uoePr3dxnuV97s8RVvImA3wC8QzTDYt4nXhq09I57xNHWUlSiM+JRwy6IPEj12WX3zgXHfbzzKiRSc8RR4mFYhvLbcxKhko8SRxTVI3y/VmXFc5bnNVylTXvyV8YymvLS1ynOYgkFrAIEQJkVLGBMizEadVIMZGm/YSHf8Dxi+SSybUBRo55VKBCcvzgf/C7W7MwMe4mhRJA54ttfwwBwV2gUbPt72PbbpwAgWfgSmv5K3Vg+pP0WkuLHQG928DFdUuT94DLHaD/SZcMyZECNP2FAvB+Rt+UAyK3QM+q21tzH6cPQIa6St0AB4fAcJGy1zze3dXe279nmv39AH+6cqz+l/YFAAANeGlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNC40LjAtRXhpdjIiPgogPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iCiAgICB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIgogICAgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIgogICAgeG1sbnM6R0lNUD0iaHR0cDovL3d3dy5naW1wLm9yZy94bXAvIgogICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iCiAgICB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iCiAgIHhtcE1NOkRvY3VtZW50SUQ9ImdpbXA6ZG9jaWQ6Z2ltcDozZWU5OTQ4My01NTBiLTRkNTItODlmNy0zMjNlNWU2NWQzZTIiCiAgIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MWRkYTM3MDAtZmI4ZS00MGQ0LThkODYtYjYzOGEwMThhZWU3IgogICB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6NmZjNzNjMzUtZmM0ZS00MGNiLTg2ZDYtZjMyYmE5NzFiNjI4IgogICBkYzpGb3JtYXQ9ImltYWdlL3BuZyIKICAgR0lNUDpBUEk9IjIuMCIKICAgR0lNUDpQbGF0Zm9ybT0iTGludXgiCiAgIEdJTVA6VGltZVN0YW1wPSIxNjk1MTMxMjY1Nzg0NzMzIgogICBHSU1QOlZlcnNpb249IjIuMTAuMzQiCiAgIHRpZmY6T3JpZW50YXRpb249IjEiCiAgIHhtcDpDcmVhdG9yVG9vbD0iR0lNUCAyLjEwIgogICB4bXA6TWV0YWRhdGFEYXRlPSIyMDIzOjA5OjE5VDIzOjE3OjQzKzA5OjMwIgogICB4bXA6TW9kaWZ5RGF0ZT0iMjAyMzowOToxOVQyMzoxNzo0MyswOTozMCI+CiAgIDx4bXBNTTpIaXN0b3J5PgogICAgPHJkZjpTZXE+CiAgICAgPHJkZjpsaQogICAgICBzdEV2dDphY3Rpb249InNhdmVkIgogICAgICBzdEV2dDpjaGFuZ2VkPSIvIgogICAgICBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjFiMTEyYjEwLTU4ZTctNGI3Zi05MGVhLTA3MDZjMjNiZTM0YiIKICAgICAgc3RFdnQ6c29mdHdhcmVBZ2VudD0iR2ltcCAyLjEwIChMaW51eCkiCiAgICAgIHN0RXZ0OndoZW49IjIwMjMtMDktMTlUMjM6MTc6NDUrMDk6MzAiLz4KICAgIDwvcmRmOlNlcT4KICAgPC94bXBNTTpIaXN0b3J5PgogIDwvcmRmOkRlc2NyaXB0aW9uPgogPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgIAo8P3hwYWNrZXQgZW5kPSJ3Ij8+zqAN3AAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAAN1wAADdcBQiibeAAAAAd0SU1FB+cJEw0vLdcy7NEAAAe9SURBVEjHzZdrbBzVFYC/OzvrfXjX633YXtsxfsQk5GEcQxCJA8GFQAspFURVQSJAEYKoiEAr8aNqWgm1UBWpoLZqgRBKRd2WRi1pAk3akAgVpWmweRliOySOvX6/vet9zu7szNz+QMSx45jQXz3S+TFz7z3fvedxz4yNxUUA1cCVgAEk+fISAK4BHEAMkItBFord4/Hcu3Xr1qtKS0tpbW1Nzs7O9n1ptFAqdzz8UEjTNI4ePdo7Ojq6B0gtCRdCfHPnzp0tlZWVHDn0JuvsHSSzJpmcNW9e54jB9o1e/vVphrXLHDjV+aaSOYv3Z2vZcsddpNNpdu/e3RWNRl883wPKArbnpptu2lRdXU0kEpGrxUeUFal80K9jWrAi7PhMyxw4CwR2m8CmwOCMTv/0nO59L8WxMxqbQv10dXURCoW4+eab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
[Rich-url]: https://rich.readthedocs.io/