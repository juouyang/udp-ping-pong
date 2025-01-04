
# UDP Ping-Pong Sidecar Container

This is a simple UDP-based ping-pong application designed to act as a sidecar container for health checks in Oracle Cloud's Network Load Balancer. The container listens on a specified UDP port and responds to "ping" messages with "pong".

## Features

- Listens for UDP packets on a specified IP and port.
- Responds to "ping" messages with "pong".
- Supports dynamic configuration for IP, port, and log verbosity.
- Lightweight and containerized for easy deployment in Kubernetes or Docker environments.

## Requirements

- Docker
- Python 3.9 (for local testing)

## Usage

### 1. Build the Docker Image

```bash
docker build -t udp-ping-pong:latest .
```

### 2. Run the Container

#### Custom IP and Port (IP: 0.0.0.0, Port: 12345)
```bash
docker run -it --rm -p 12345:12345/udp --name udp-ping-pong udp-ping-pong:latest 0.0.0.0 12345
```

#### Silent Mode
To suppress log output:
```bash
docker run -it --rm -p 12345:12345/udp --name udp-ping-pong udp-ping-pong:latest 0.0.0.0 12345 --silent
```

### 3. Test the Server

To test the UDP server locally, use the included `client_UDP.py` script:

```bash
python3 client_UDP.py <server-ip> 12345
```

Replace `<server-ip>` with the IP address of the running container or server.

### 4. Deploy as a Sidecar in Kubernetes

To use this container as a sidecar in a Kubernetes deployment, add it to your Pod specification with the following example:

```yaml
containers:
  - name: udp-ping-pong
    image: juouyang/udp-ping-pong:latest
    args: ["0.0.0.0", "12345", "--silent"]
    ports:
      - containerPort: 12345
        protocol: UDP
```

## Environment

- **Server Script**: `server_UDP.py`
- **Default IP**: 0.0.0.0
- **Default Port**: 12345 (can be modified at runtime)

## Health Check in Oracle Cloud

1. Configure your Oracle Network Load Balancer to point to this container's exposed UDP port (e.g., 12345).
2. Set the health check payload to `"ping"`.
3. The container will respond with `"pong"` for successful checks.

## License

MIT License. Feel free to use and modify.
