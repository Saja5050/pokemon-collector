# 🎮 Pokemon Collector

A modern web application for collecting and discovering Pokemon using the PokeAPI. Built with Flask and featuring a beautiful, responsive UI.

## ✨ Features

- **Random Pokemon Drawing**: Discover new Pokemon with each draw
- **Collection Management**: View and search your collected Pokemon
- **Beautiful UI**: Modern, responsive design with animations
- **Data Persistence**: Pokemon data saved in JSON format
- **PokeAPI Integration**: Real-time Pokemon data fetching

## 🚀 Quick Start

### Option 1: Automatic Deployment (Recommended)

Run the deployment script on a fresh Ubuntu server:

```bash
# Download and run deployment script
curl -sSL https://raw.githubusercontent.com/YOUR_USERNAME/pokemon-collector/main/deploy.sh | sudo bash
```

### Option 2: Manual Installation

1. **Clone the repository**:
```bash
git clone https://github.com/YOUR_USERNAME/pokemon-collector.git
cd pokemon-collector
```

2. **Create virtual environment**:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the application**:
```bash
python app.py
```

5. **Access the app**:
Open your browser and go to `http://localhost:8080`

## 📁 Project Structure

```
pokemon-collector/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── deploy.sh          # Automatic deployment script
├── pokemons.json      # Pokemon collection data (auto-generated)
├── templates/         # HTML templates
│   ├── index.html     # Home page
│   ├── result.html    # Pokemon display page
│   ├── collection.html # Collection view
│   └── exit.html      # Goodbye page
└── static/           # Static files (if any)
```

## 🎯 How It Works

1. **Draw Pokemon**: Click "Draw Pokemon" to get a random Pokemon
2. **Data Check**: App checks if Pokemon exists in local JSON database
3. **Fetch Details**: If new, fetches Pokemon details from PokeAPI
4. **Save & Display**: Saves to JSON and displays Pokemon information
5. **Collection View**: Browse all collected Pokemon with search functionality

## 📊 Data Schema

Each Pokemon is stored with the following attributes:

```json
{
  "name": "pikachu",
  "height": 4,
  "weight": 60,
  "types": ["electric"],
  "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
}
```

## 🛠️ API Endpoints

- `GET /` - Home page
- `GET /draw` - Draw a random Pokemon
- `GET /collection` - View Pokemon collection
- `GET /exit` - Farewell page

## 🔧 Configuration

### Environment Variables

- `FLASK_ENV`: Set to `development` for debug mode
- `PORT`: Custom port (default: 8080)

### Customization

- **Pokemon API**: Uses [PokeAPI](https://pokeapi.co/) for Pokemon data
- **Data Storage**: JSON file (`pokemons.json`) for simplicity
- **UI Themes**: Easily customizable CSS in HTML templates

## 🚀 Deployment Features

The automatic deployment script includes:

- ✅ **Infrastructure Provisioning**: Server setup and security configuration
- ✅ **Automatic Installation**: Clones from GitHub and installs dependencies
- ✅ **Service Management**: Systemd service for automatic startup
- ✅ **Reverse Proxy**: Nginx configuration for production
- ✅ **Firewall Setup**: UFW firewall with proper port configuration
- ✅ **Welcome Message**: Usage instructions shown on SSH login
- ✅ **Health Checks**: Automatic testing of deployment

## 📋 Server Management

After deployment, use these commands:

```bash
# Service management
sudo systemctl start pokemon-collector
sudo systemctl stop pokemon-collector
sudo systemctl restart pokemon-collector
sudo systemctl status pokemon-collector

# View logs
sudo journalctl -u pokemon-collector -f

# Update application
cd /opt/pokemon-collector
sudo -u pokemon git pull
sudo systemctl restart pokemon-collector
```

## 🧪 Testing

### Manual Testing

1. **Home Page**: Verify all Pokemon sprites load
2. **Draw Function**: Test random Pokemon drawing
3. **Collection**: Check collection view and search
4. **Data Persistence**: Verify Pokemon data saves to JSON

### Automated Testing

```bash
# Test local connection
curl http://localhost:8080

# Test specific endpoints
curl http://localhost:8080/draw
curl http://localhost:8080/collection
```

## 🔒 Security Features

- **Firewall Configuration**: Only necessary ports open
- **Service User**: App runs under dedicated user account
- **Input Validation**: Secure handling of user input
- **Reverse Proxy**: Nginx handles external connections

## 🐛 Troubleshooting

### Common Issues

1. **Service not starting**:
```bash
sudo journalctl -u pokemon-collector
```

2. **Port conflicts**:
```bash
sudo netstat -tlnp | grep 8080
```

3. **Permission issues**:
```bash
sudo chown -R pokemon:pokemon /opt/pokemon-collector
```

### Logs Location

- Application logs: `sudo journalctl -u pokemon-collector`
- Nginx logs: `/var/log/nginx/error.log`
- System logs: `/var/log/syslog`

## 📈 Performance

- **Caching**: Pokemon data cached in JSON for faster access
- **Static Files**: Served directly by Nginx
- **Compression**: Gzip compression enabled
- **Connection Pooling**: Efficient HTTP connections to PokeAPI

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [PokeAPI](https://pokeapi.co/) for the amazing Pokemon data
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Bootstrap](https://getbootstrap.com/) for responsive design components

## 📞 Support

For issues and questions:

1. Check the troubleshooting section above
2. Review the server logs
3. Open an issue on GitHub
4. Check PokeAPI status at https://pokeapi.co/

---

**Happy Pokemon Collecting! 🎉**