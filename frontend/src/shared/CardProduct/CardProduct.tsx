import {Card, CardHeader, CardBody, Image} from "@nextui-org/react";

export function CardProduct({ product }) {
    return (
        <Card className="py-4 max-w-64 w-full m-2" style={{ maxWidth: '250px', maxHeight: '350px' }}>
            <CardHeader className="pb-0 pt-2 px-4 flex-col items-start">
                <h5 className="font-bold text-large">{product.name}</h5>
                <small className="text-default-500">{product.price}$</small>
            </CardHeader>
            <CardBody className="overflow-visible py-2">
                <Image
                    alt="Card background"
                    className="object-cover rounded-xl"
                    src={product.image}
                    width={240}
                />
            </CardBody>
        </Card>
    )
}