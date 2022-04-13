FROM 58paul/centos-vnc:latest
ADD Python-3.7.1.tgz /opt/
#RUN cd /opt/Python-3.7.1 && ./configure --prefix=/usr/local/python3
RUN mkdir /usr/local/python3 && mkdir /data && rm -rf /etc/yum.repos.d/* 
COPY test.py /data/
COPY CentOS-Base.repo /etc/yum.repos.d/	
COPY epel.repo /etc/yum.repos.d/
RUN yum makecache && \
    yum install gcc gcc-c++ make cmake zlib zlib-devel bzip2 bzip2-devel sqlite sqlite-devel openssl \
        openssl-devel libffi-devel libffi-devel -y && \
    yum clean all
RUN /opt/Python-3.7.1/configure --prefix=/usr/local/python3 && \
    make && \
    make install
RUN ln -s /usr/local/python3/bin/python3 /usr/bin/python3 && \
    ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
RUN pip3 install pyppeteer


