export const CLIENT_ID = "4b68805ec6354a768f40203e45e8982b";
export const SPOTIFY_AUTHORIZE_ENDPOINT = "https://accounts.spotify.com/authorize";
export const REDIRECT_URL_AFTER_LOGIN = "http://localhost:3000/home";
export const SPACE_DELIMETER = "%20";
export const SCOPES = [
   // "playlist-read-public",
   "playlist-modify-public"
];
export const SCOPES_URL_PARAM = SCOPES.join(SPACE_DELIMETER);