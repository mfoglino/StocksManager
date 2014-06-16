package hello;

import org.springframework.context.annotation.Bean;


public class MessageServiceImpl implements MessageService {

	public String getMessage() {
		return "MessageServiceImpl";
	}

}
