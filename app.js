const [plants, setPlants] = useState([]);

useEffect(() => {
  fetch('/plants')
    .then(response => response.json())
    .then(data => setPlants(data));
}, []);

return (
  <div>
    {plants.map(plant => (
      <div key={plant.id}>
        <h2>{plant.name}</h2>
        <img src={plant.image_url} alt={plant.name} />
        <p>{plant.description}</p>
      </div>
    ))}
  </div>
);
