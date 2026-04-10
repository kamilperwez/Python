export default async function handler(req, res) {
    const { q, offset } = req.query;
    // This pulls the key from Vercel's hidden environment variables
    const apiKey = process.env.GIPHY_KEY; 
    
    const url = `https://api.giphy.com/v1/gifs/search?api_key=${apiKey}&q=${q}&limit=1&offset=${offset}&rating=g`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        res.status(200).json(data);
    } catch (error) {
        res.status(500).json({ error: "Failed to fetch" });
    }
}