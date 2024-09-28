import { SPOTIFY_CLIENT_ID } from "./credentials";

export const CLIENT_ID = SPOTIFY_CLIENT_ID;
export const SPOTIFY_AUTHORIZE_ENDPOINT = "https://accounts.spotify.com/authorize";
export const REDIRECT_URL_AFTER_LOGIN = "http://localhost:3000/home";
export const SPACE_DELIMETER = "%20";
export const SCOPES = [
   "playlist-modify-public"
];
export const SCOPES_URL_PARAM = SCOPES.join(SPACE_DELIMETER);