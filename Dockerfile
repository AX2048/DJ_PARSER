FROM python:3.10.9
# 

# Install Chrome WebDriver
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

# Install Google Chrome
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get -yqq update && \
    apt-get -yqq install google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /code

# set environment variables
# запрещает Python записывать файлы pyc на диск python -B
#ENV PYTHONDONTWRITEBYTECODE 1
# запрещает Python буферизовать stdout и stderr python -B
#ENV PYTHONUNBUFFERED 1

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN python3 -m pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./mysite /code/mysite
COPY ./chrome_drv/ /code/chrome_drv/

#
ENV DISPLAY=:99
#ENV PATH /usr/local/bin:$PATH

# 
CMD ["python3", "mysite/manage.py", "runserver", "0.0.0.0:8000", "--noreload"]

# docker run -p 80:8000 webpro1