import { User, } from "@/api/models";


type AllowedMethod = "GET" | "POST" | "DELETE" | "PUT" | "PATCH";


export interface EndpointInterface<T = unknown> {
    endpoint: string;
    method: AllowedMethod;
    body?: T;
}

export class BackendEndpoint {

    static readonly CreateUser: (
        body: User
    ) => EndpointInterface<User> = body => {
        return {
            endpoint: "/v1/authorized-users",
            method: "POST",
            body: body,
        };
    };

    static readonly GetUsers: EndpointInterface = {
        endpoint: "/v1/authorized-users",
        method: "GET",
    };

    static readonly Logout: EndpointInterface = {
        endpoint: "/users/logout",
        method: "GET",
    };

}
