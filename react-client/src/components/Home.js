import axios from 'axios';

function Home() {
   function generatePlaylist() {
      console.log(localStorage.getItem("accessToken"));
      const config = {
         headers: {
            'Content-Type': 'application/json',
            'Authorization': localStorage.getItem("accessToken"),
         }
      }

      axios.get("http://localhost:5000/playlists", config).then(res => {
         console.log(res);
      });
   }

   return (
      <div>
         <h1>Home Page. Get your music!</h1>
         <button onClick={generatePlaylist}>Generate Playlist!</button>
      </div>
   );
}

export default Home;