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
            endpoint: "/v0/user",
            method: "POST",
            body: body,
        };
    };

    static readonly GetUser: EndpointInterface = {
        endpoint: "/v0/user",
        method: "GET",
    };

}
