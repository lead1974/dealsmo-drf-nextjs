import { baseApiSlice } from "./api/baseApiSlice";
import authReducer from "@/lib/redux/features/auth/authSlice";

export const rootReducer = {
	[baseApiSlice.reducerPath]: baseApiSlice.reducer,
	auth: authReducer,
};